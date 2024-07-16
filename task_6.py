types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def remove_duplicates(tickets):
    seen_tickets = set()
    new_tickets = {}
    for priority, ticket_list in sorted(tickets.items()):
        new_tickets[priority] = []
        for ticket in ticket_list:
            if ticket not in seen_tickets:
                seen_tickets.add(ticket)
                new_tickets[priority].append(ticket)
    return new_tickets

def map_tickets(types, tickets):
    tickets = remove_duplicates(tickets)
    return {types[key]: value for key, value in tickets.items()}

def run6():
    print(map_tickets(types, tickets))