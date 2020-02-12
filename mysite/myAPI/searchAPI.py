#-*-coding:utf-8-*-
#查询字段name|contact
def SearchNameContact(model, name,contact):
    if name:
        return model.objects.filter(name__icontains=name)
    if contact:            
        return model.objects.filter(contact__icontains=contact)
    return model.objects.all()