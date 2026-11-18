JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "Al Adl Website Admin",
    # Title on the brand, and the login screen (19 chars max)
    "site_header": "Al Adl Website",
    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    "site_logo": "website/img/logo.webp",
    # Welcome text on the login screen
    "welcome_sign": "Al Adl Website Admin",
    # Copyright on the footer
    "copyright": "🔥 Powered by NullStack Technologies",
    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "website.ServiceModel",
    # Field name on user model that contains avatar image
    "user_avatar": None,
    ############
    # Top Menu #
    ############
    # Links to put along the top menu
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Website", "url": "https://aladllegal.com"},
        # external url that opens in a new window (Permissions can be added)
        # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        # model admin to link to (Permissions checked against model)
        # {'model': 'auth.User', 'name': 'All users'},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "shop"},
    ],
    #############
    # User Menu #
    #############
    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    "usermenu_links": [
        # {'name': 'Support', 'url': 'https://nullstacks.com', 'new_window': True},
        # {'model': 'auth.user'}
    ],
    #############
    # Side Menu #
    #############
    # Whether to display the side menu
    "show_sidebar": True,
    # Whether to aut expand the menu
    "navigation_expanded": True,
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [
        "account",
        "taggit",
        "flatpages",
        "auth",
        # 'wagtaildocs',
        # 'wagtailimages',
        # 'taggit',
    ],
    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],
    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        "constance",
        "payment",
        "subscription",
        "index",
        "question_papers",
        "test_series",
        "auth",
        "authentication",
        # "generic", "promotions", "shop"
    ],
    # Custom links to append to app groups, keyed on app name
    # 'custom_links': {
    #     'polls': [{
    #         'name': 'Make Messages',
    #         'url': 'make_messages',
    #         'icon': 'fas fa-comments',
    #         'permissions': ['polls.view_poll']
    #     }]
    # },
    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "constance.Config": "fas fa-cog",
        "website.EnquiryModel": "fas fa-business-time",
        "website.ServiceModel": "fas fa-plus-square",
        "website.TeamModel": "fas fa-users",
        "website.FAQModel": "fas fa-info",
        "blog.BlogModel": "fas fa-pen",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,
    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    # Add a language dropdown into the admin
    # "language_chooser": True,
    "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-light",
    "accent": "accent-info",
    "navbar": "navbar-light",
    "no_navbar_border": True,
    "sidebar": "sidebar-light-warning",
    "sidebar_nav_small_text": True,
    "sidebar_disable_expand": True,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    # "theme": "simplex",
}
