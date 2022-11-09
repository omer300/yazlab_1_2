columns = ['Product','Issue','Company','State','ZIP code','Complaint ID']
f=pd.read_csv("rows.csv", usecols=columns, dtype={'Product' : 'string',
                                                        'Issue'  : 'string',
                                                        'Company' : 'string',
                                                        'State'  : 'string',
                                                        'ZIP code' : 'string',
                                                        'Complaint ID'  : 'int64',
})

print(f)
