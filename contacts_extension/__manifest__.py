{
    "name": "contacts_extension",
    "version": "0.1",
    "summary": "LIESA Contacts extension",
    "description": "Modulo de extensión de la gestión de contactos (empresas y personas)",
    "depends": ["base", "contacts"],
    "data": [
        "views/segment_views.xml",
        "views/res_partner_views.xml",
        "security/ir.model.access.csv",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
