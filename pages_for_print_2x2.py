# init
FIRST_PAGE = 880
LAST_PAGE = 895
PAGES_PER_SIDE = 2
SIDES = 2
sides = list(range(SIDES))
PAGES_PER_SHEET = PAGES_PER_SIDE * SIDES
# lists with pages
pages = list()
for i in sides:
    pages.append([])

def sheet_side(num):
    return num // PAGES_PER_SIDE

for page in range(FIRST_PAGE, LAST_PAGE+1, PAGES_PER_SHEET):
    for i in range(PAGES_PER_SHEET):
        current_page = page + i
        if current_page <= LAST_PAGE:
            pages[sheet_side(i)].append(current_page)

num_sheets = 0
for i in range(SIDES):
    output = ""
    for imprint_index in range(len(pages[i])):
        sepr = ","
        #
        if PAGES_PER_SIDE - imprint_index % PAGES_PER_SIDE == 1:
            sepr = ", "
        output += str(pages[i][imprint_index]) + sepr
        #
        if i == 0 and imprint_index % PAGES_PER_SIDE == 0:
            num_sheets += 1
    print(output.strip(", "))
print(num_sheets)
        
