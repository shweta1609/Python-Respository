def generate_bio(line):
    dict_bio = {}
    fields = line.split(',')
    dict_bio['name'] = fields[0].lstrip('"').replace('""','"').replace('""','"')
    dict_bio['age'] = fields[len(fields)-1].rstrip('\n')
    i = 3
    if fields[i].startswith('"'):
        dict_bio['interests'] = fields[3].lstrip('"')
        i += 1
        while (not fields[i].endswith('"')):
            dict_bio['interests']+=fields[i]
            dict_bio['interests']+=","
            i+=1
        dict_bio['interests']+=","
        dict_bio['interests']+=fields[i].rstrip('"')
    else:
        dict_bio['interests'] = fields[i]
    i+=2
    if fields[i].startswith('"'):
        dict_bio['address'] = fields[i].lstrip('"')
        dict_bio['address'] += ","
        i+=1
        while (not fields[i].endswith('"')):
            dict_bio['address']+= fields[i]
            dict_bio['address'] += ","
            i+=1
        dict_bio['address']+=fields[i].rstrip('"')
    else:
        dict_bio['address'] = fields[i]
    bio = dict_bio['name'] + ", " + dict_bio['age'] + " years old," + " is from "+ dict_bio['address'] + " and is interested in "+ dict_bio['interests']+"."
    print(bio)

for lines in sys.stdin:
    generate_bio(lines)
