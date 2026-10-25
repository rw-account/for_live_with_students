from flask import Blueprint, abort, render_template


bp = Blueprint('test', __name__, url_prefix='/test')

# عدّل بيانات التحديات أو أضف تحديات أخرى هنا.
CHALLENGES = [
    {
        'id': 1,
        'arabic_number': 'الأول',
        'summary': 'التحقق من السعر ومصدره في تطبيق تدريبي محلي.',
        'available': True,
        'title': 'التحقق من السعر في جهة الخادم',
        'idea': 'لا ينبغي للتطبيق أن يثق في قيمة السعر القادمة من المتصفح؛ يجب أن يستخرج السعر المعتمد من بيانات الخادم ويتحقق من الطلب قبل إتمام الشراء.',
        'scenario': 'استخدموا حصراً محاكاة محلية أو مختبر تدريب مصرحاً به، يحتوي على منتج تجريبي سعره 100 دولار. لا تختبروا متجراً حقيقياً أو نظاماً لا تملكون إذناً صريحاً لاختباره.',
        'task': 'حلّلوا في المختبر كيف تُرسل بيانات عملية الشراء، ثم ناقشوا: هل يعتمد التطبيق على بيانات يرسلها العميل أم يعيد التحقق من سعر المنتج في الخادم؟ دوّنوا نتيجة الاختبار واشرحوا كيف ينبغي أن يمنع التحقق من جهة الخادم تغيير السعر.',
        'goal': 'فهم مخاطر الثقة بمدخلات العميل، والتمييز بين التحقق في المتصفح والتحقق الإلزامي في الخادم.',
    },
    {
        'id': 2,
        'arabic_number': 'الثاني',
        'summary': 'بيانات مؤقتة — أضف فكرة التحدي لاحقاً.',
        'available': False,
    },
    {
        'id': 3,
        'arabic_number': 'الثالث',
        'summary': 'بيانات مؤقتة — أضف فكرة التحدي لاحقاً.',
        'available': False,
    },
]


@bp.route('/')
def index():
    """يعرض قائمة التحديات على /test/."""
    return render_template('test/index.html', challenges=CHALLENGES)


@bp.route('/challenge/<int:challenge_id>')
def challenge_detail(challenge_id):
    """يعرض تفاصيل تحدٍ محدد."""
    challenge = next(
        (item for item in CHALLENGES if item['id'] == challenge_id),
        None,
    )
    if challenge is None:
        abort(404)
    return render_template('test/challenge.html', challenge=challenge)