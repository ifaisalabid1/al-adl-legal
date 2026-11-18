from collections import OrderedDict

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

CONSTANCE_ADDITIONAL_FIELDS = {
    'image_field': ['django.forms.ImageField', {}]
}

CONSTANCE_CONFIG = OrderedDict([
    # Company Settings
    ('COMPANY_LOGO', (
        'https://aladllegal.com/wp-content/uploads/2022/04/logoresized.png',
        'Company Logo',
    )),
    ('COMPANY_SITE_HEADER', (
        'Al Adl Legal',
        ''
    )),
    ('COMPANY_SITE_TITLE', (
        'Al Adl Legal',
        ''
    )),
    ('COMPANY_WEBSITE', (
        'https://aladllegal.com',
        ''
    )),

    # SEO Settings
    ('COMPANY_SEO_INDEX_TITLE', (
        '',
        ''
    )),
    ('COMPANY_SEO_DESCRIPTION', (
        '',
        ''
    )),
    ('COMPANY_SEO_KEYWORDS', (
        '',
        ''
    )),
    ('COMPANY_SEO_IMAGE', (
        '',
        'URL For Company SEO Image'
    )),

    # Email Settings
    ('COMPANY_ADMIN_EMAILS', (
        'info@aladllegal.com',
        'A comma separated value of The Admin Who will manage the customers',
    )),
])
