# -*- coding: utf-8 -*-
######################################################################################
#
#    Captivea
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################

{
    'name': 'CAP PLM Enhancements',
    'version': '15.0.0.2',
    'summary': 'Enhances product lifecycle management and related model functionality',
    'description': """Refer to index.html file for references to tickets covered in this module
                """,
    'category': 'Product Lifecycle Management',
    'author': 'Captivea LLC, BEL',
    'company': 'Captivea LLC',
    'maintainer': 'https://www.captivea.com/',
    'depends': 
    ['base',
     'mrp_plm',
     'mrp',
     'product',
     'stock',
     'account',
     'sale_product_configurator',
     'mail',
    ],
    'website': 'https://www.captivea.com/',
    'data': [
        'views/plm_view.xml',
        'data/mrp_eco_stage_data.xml',
    ],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': False,
    "cloc_exclude": ["./**/*"],  # exclude all files in a module recursively
}
