{
    'name':'ht_in_reports',
    'version':'14.0.0.1.0',
    'summary':'IN Reports',
    'Author':'Ruchita Sapariya',
    'description':'''Indian standard PDF reports.''',
    'website':'http.google.com',
    'depends':['sale','base'],
    'data':[
        
        'security/ir.model.access.csv',
        'data/seq_report_invoice.xml',
        'views/report_views.xml',
        'reports/invoice_report.xml',
        
    ],
    'installable': True,
    'auto_install': False,
}
