from flask import Blueprint, abort, render_template, request


bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route('/')
def index():
    return render_template('test/index.html')


@bp.route('/challenge/1', methods=['GET', 'POST'])
def challenge_1():
    if request.method == 'POST':
        price = request.form.get('price', '')

        return f"""
        <!DOCTYPE html>
        <html lang="ar" dir="rtl">
        <head>
            <meta charset="UTF-8">
            <title>نجاح العملية</title>
        </head>
        <body>
            <h1>تم الشراء بنجاح!</h1>
            <p>تم إرسال سعر الآيفون بنجاح: {price}</p>
        </body>
        </html>
        """

    return render_template('test/challenge1.html')

@bp.route('/challenge/2')
def challenge_2():
    return render_template('test/challenge2.html')


@bp.route('/challenge/2/dashboard')
def challenge_2_dashboard():
    role = request.args.get('role', '')

    if role != 'admin':
        abort(403, description='تم رفض الوصول: لا تملك الصلاحية المطلوبة.')

    return '<h1 dir="rtl">تهانينا! لقد نجحت في الوصول إلى لوحة تحكم المسؤول.</h1>'