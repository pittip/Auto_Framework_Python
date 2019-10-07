from enum import Enum

class MainPage(Enum):
    TO_ABTESTING_PAGE               = "//a[starts-with(@href, '/abtest')]"
    TO_ADD_REMOVE_ELEMENTS_PAGE     = "//a[starts-with(@href,'/add_remove_elements/')]"
    TO_BROKEN_IMAGES_PAGE           = "//a[starts-with(@href, '/broken_images')]"
    TO_CHALLENGING_DOM_PAGE         = "//a[starts-with(@href, '/challenging_dom')]"
    TO_CHECKBOXES_PAGE              = "//a[starts-with(@href, '/checkboxes')]"
    TO_CONTEXTMENU_PAGE             = "//a[starts-with(@href, '/context_menu')]"
    TO_DISAPPEARING_ELEMENTS_PAGE   = "//a[starts-with(@href, '/disappearing_elements')]"


