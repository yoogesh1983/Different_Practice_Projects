from django import template
register = template.Library()

@register.filter(name='ymsTruncate5')
def truncate5(input):
    return input[0:5]

@register.filter(name='ymsTruncateN')
def truncateN(input, number):
    return input[0:number]


#registering our custom filter into a template filter (if you do not provide the annotation)
#register.filter('ymsTruncate5', truncate5)
#register.filter('ymsTruncateN', truncateN)
