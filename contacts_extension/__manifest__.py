{
    "name": "contacts_extension",
    "version": "0.1",
    "summary": "LIESA Contacts extension",
    "description": "Modulo de extensión de la gestión de contactos (empresas y personas)",
    "depends": ["base", "contacts"],
    "data": [
        "data/categories.xml",
        "views/segment_views.xml",
        "views/res_partner_views.xml",
        "security/contact.groups.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "assets": {
        # "mail.assets_discuss_public": [
        #     "contacts_extension/static/src/components/chatter_topbar/chatter_topbar.xml",
        # ],
        # "web.assets.backend": [
        #     "contacts_extension/static/src/components/chatter_topbar/chatter_topbar.xml",
        # ],
        "web.assets_qweb": [
            "contacts_extension/static/src/xml/chatter.xml",
        ],
    },
    "license": "LGPL-3",
}
