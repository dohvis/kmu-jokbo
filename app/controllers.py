from flask import (
    flash,
    redirect,
    render_template,
    request,

)
from app import (
    app,
    aws_session,
)
from app.forms import ExamUploadForm
from app.models import Exam
from app.utils import sha256


@app.route('/', methods=['GET'])
def index():
    exams = Exam.objects.all()
    return render_template('index.html', exams=exams)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = ExamUploadForm()
    if request.method == 'GET':
        return render_template('upload.html', form=form)

    if not form.validate_on_submit():
        return render_template('upload.html', form=form)

    uploaded_file = request.files['file_']
    ext = uploaded_file.filename.split('.')[-1]  # pdf, docx, etc..
    filename = '{}-{}-{}년-{}학기-{}고사.{}'.format(
        form.subject.data,
        form.professor.data,
        form.year.data,
        form.semester.data,
        form.case.data,
        ext,
    )
    print(filename, len(filename))

    obj_key = 'files/'.format(
        form.subject.data,

    )

    s3 = aws_session.resource('s3')
    s3_bucket = s3.Bucket(app.config.get('AWS_S3_BUCKET_NAME'))
    s3_bucket.put_object(
        ACL='public-read',
        Body=uploaded_file.stream.read(),
        Key=obj_key,
        ContentType=uploaded_file.mimetype,
        Metadata={
            'owner-content-type': 'document'
        }
    )
    Exam(
        key=filename,
        subject=form.subject.data,
        professor=form.professor.data,
        year=form.year.data,
        semester=form.semester.data,
        case=form.case.data,
        file_format=ext,
    ).save()

    flash('시험 정보가 성공적으로 업로드 되었습니다. 감사합니다 :)')
    return redirect('/')


@app.route('/status')
def status():
    # For AWS Health check
    return 'OK'
