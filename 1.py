def quickFind(request, deviceId):
    db = 'compatibilityTest'
    conn = MySQLdb.connect(host=host, port=port, user=user, passwd=passwd,
                           db=db, charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor)
    cursor = conn.cursor()
    deviceId = deviceId.strip()
    sql = "select deviceBrand, device, id, os, ram from deviceInfo \
        where id like \'%%%s%%\'" % (deviceId)
    cursor.execute(sql)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    if res:
        phone = res[0]

        tmp = "（%s）" %(phone['id'])
        phone['device'] = phone['device'].replace(tmp, '')

        if 'M' in phone['ram']:
            phone['ram'] = '小于1GB'
        elif 'G' in phone['ram']:
            tmp = ''.join([c for c in phone['ram'] if c.isdigit() or c == '.'])
            phone['ram'] = tmp + 'GB'
        else:
            phone['ram'] = '未知'

        phone['type'] = phone['os'].split()[0]
        type_dict = {'ios' : 'iOS',
                     'android' : 'Android',
                     'windows' : 'Windows',
                     'watch' : 'Watch OS',
                     'flyme' : 'Flyme',
                     }
        if phone['type'].lower() in type_dict:
            phone['type'] = type_dict[phone['type'].lower()]

    else:
        phone = ''
    jsonRes = JSONEncoder().encode(phone)
    return HttpResponse(jsonRes)