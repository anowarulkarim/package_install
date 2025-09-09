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
            db_name = self.env.cr.dbname
            name=db_name.split('_')[0]
            if response.status_code==200:
                file_path = f"/opt/odoo-on-docker/install.txt"
                file_content=f"""
{name} {record.name}
"""
                with open(file_path,'a') as f:
                    f.write(file_content)
            else:
                raise ValidationError(_("This is not a valid package name. Check properly"))

            record.state = "installed"

