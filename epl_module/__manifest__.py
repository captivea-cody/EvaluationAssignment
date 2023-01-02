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
    'name': 'EPL Data Module',
    'version': '15.0.0.2',
    'summary': 'A bunch of silly soccer faff.',
    'description': """Soccer is cool
                """,
    'category': 'Evaluation Assignment',
    'author': 'Captivea LLC, Cody Wiggins',
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
        'views/epl_view.xml',
        'data/club_nat_player_data.xml',
    ],
    'qweb': [],
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    "cloc_exclude": ["./**/*"],  # exclude all files in a module recursively
}
