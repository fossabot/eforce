from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''


@register.simple_tag
def google_api_key():
    from eforce.settings import GOOGLE_SERVICE_API_KEY
    return GOOGLE_SERVICE_API_KEY


@register.simple_tag
def cmo_api_url():
    from eforce.settings import CONST_CMO_DOMAIN
    return CONST_CMO_DOMAIN


@register.simple_tag
def ef_assets_user_instructions(user):
    from eforce_front.views.get_context_views import get_user_group_unread_instructions
    return get_user_group_unread_instructions(user)


@register.simple_tag
def get_unread_hq_crisises():
    from eforce_front.views.get_context_views import get_unread_crisises
    return get_unread_crisises()


@register.simple_tag
def get_unread_crisis_updates():
    from eforce_front.views.get_context_views import get_unread_efassets_updates
    return get_unread_efassets_updates()


@register.simple_tag
def get_unread_combat_strategies():
    from eforce_front.views.get_context_views import get_unread_cmo_combat_strategies
    return get_unread_cmo_combat_strategies()


@register.simple_tag
def get_humanize_datetime(datetime):
    import humanize
    from django.utils import timezone
    return humanize.naturaltime(timezone.now() - datetime)


@register.simple_tag
def google_map_page_link():
    return "https://www.google.com.sg/maps/dir//"
