from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from eforce_api.models import Crisis, InstructionGroupAssoc, CrisisUpdate
import operator


class CrisisInstructions():

    def __init__(self, crisis):
        self.crisis = crisis
        self.datetime = crisis.created_datetime
        self.crisis_locations = crisis.affected_locations.all()
        self.instructions = []

    def add_instruction(self, instruction):
        self.instructions.append(instruction)


def get_EF_HQ_crisis():
    return Crisis.objects.all()


def get_user_group_crisis_instructions(user):
    crisis_instructions = {}
    instructions = user.userprofile.get_group_instruction_notification()
    for instr in instructions:
        crisis_pk = instr.for_strategy.crisis.pk
        if not crisis_instructions.__contains__(crisis_pk):
            newCrisisInstructions = CrisisInstructions(crisis=instr.for_strategy.crisis)
            newCrisisInstructions.add_instruction(instr)
            crisis_instructions[crisis_pk] = newCrisisInstructions
        else:
            crisis_instructions[crisis_pk].add_instruction(instr)

    return (sorted(crisis_instructions.values(), key=operator.attrgetter('datetime'), reverse=True))


def get_user_group_unread_instructions(user):

    i = InstructionGroupAssoc.objects.filter(has_read=False,
                                             to_group=user.userprofile.usergroup)

    return i.order_by('instruction')


def get_unread_crisises():
    i = Crisis.objects.filter(has_read=False)
    return i


def get_this_efasset_usergroup_sent_updates_by_page(request):
    efassets_updates = CrisisUpdate.objects.filter(by_group=request.user.userprofile.usergroup)
    page = request.GET.get('page', 1)
    paginator = Paginator(efassets_updates, 20)

    try:
        sent_updates = paginator.page(page)
    except PageNotAnInteger:
        sent_updates = paginator.page(1)
    except EmptyPage:
        sent_updates = paginator.page(paginator.num_pages)

    return sent_updates
