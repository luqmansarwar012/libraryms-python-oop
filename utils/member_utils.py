from member.member import Member
from .get_int_input import get_int_input


def create_member():
    member_id = get_int_input("Enter member id\n")
    name = input("Enter member name\n")
    member = Member(member_id, name)
    return member
