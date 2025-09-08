from odoo import api, fields, models,_
import requests
from odoo.exceptions import ValidationError

class PackageInstall(models.Model):
    _name = 'package.install'
    _description = 'Python Package Installer'

    name = fields.Char(
        string='Python Package Name',
        required=True,
        help="Name of the Python package you want to install"
    )

    state = fields.Selection(
        [
            ('pending', 'Pending'),
            ('installed', 'Installed'),
            ('failed', 'Failed')
        ],
        string="Status",
        default="pending",
        readonly=True
    )


    def accept(self):
        """ Trigger package installation (to be implemented) """
        for record in self:
            # Placeholder logic

            url = f"https://pypi.org/pypi/{record.name}/json"
            response = requests.get(url)

            if response.status_code==200:
                pass
            else:
                raise ValidationError(_("This is not a valid package name. Check properly"))

            record.state = "installed"

