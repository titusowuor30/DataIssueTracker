from datetime import datetime

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "DQITs Admin",

    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "DQITs Administration",

    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Admin",

    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "/logo/logo.png",

    # CSS classes that are applied to the logo above
    "site_logo_classes": "img-circle img-fluid",

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    "site_icon": "/logo/logo.png",

    # Welcome text on the login screen
    "welcome_sign": "Welcome to DQITs Admin",

    # Copyright on the footer
    "copyright": f"Copyright © DQITs @ {datetime.now().year}. All Rights reserved.",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "DQITAuth.CustomUser",

    # Field name on user model that contains avatar ImageField/URLField/Charfield or a callable that receives the user
    "user_avatar": "/logo/logo.png",

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "/user/home", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://bengohub.co.ke", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "DQITAuth.CustomUser"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "DQIT_Endpoint"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    #https://github.com/farridav/django-jazzmin/issues
    "usermenu_links": [
        {"name": "Support", "url": "https://bengohub.co.ke", "new_window": True},
        {"model": "DQITAuth.CustomUser"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": True,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g authman.CustomUser)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": ["account","auth.group"],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        "DQIT_Endpoint": [{
            "name": "Make Messages",
            "url": "DQIT_Endpoint",
            "icon": "fas fa-comments",
            "permissions": ["DQIT_Endpoint.view_book"]
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    "icons": {
        "auth.group": "fas fa-users",
        "DQITAuth.CustomUser": "fas fa-user",
        "DQITAuth.roles": "fas fa-users",
        "DQITAuth.passwordpolicy": "fas fa-lock",
        "DQITAuth.backupschedule": "fas fa-database",
        "DQIT_Endpoint.DataSyncSettings": "fas fa-sync",
        "DQIT_Endpoint.EmailSetup": "fas fa-inbox",
        "DQIT_Endpoint.Facilities": "fas fa-list",
        "DQIT_Endpoint.DataQualityIssues": "fas fa-list",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-check-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

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
    "changeform_format_overrides": {"DQITAuth.CustomUser": "collapsible", "auth.group": "vertical_tabs"},
    # Add a language dropdown into the admin
    #"language_chooser": True,
}
