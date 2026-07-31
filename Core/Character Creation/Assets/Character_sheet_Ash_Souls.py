"""
character_sheet_final_v10.py
Final layout with correct scaling and positions for Ash&Souls campaign.
"""

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import black, gray, Color

# -------------------- Constants --------------------
W, H = A4
MARGIN = 2 * mm
GUTTER = 2 * mm
BORDER_WIDTH = 0.5
HEADER_SIZE = 14
LABEL_SIZE = 10
FIELD_HEIGHT = 10 * mm
MULTILINE_FIELD_HEIGHT = 30 * mm
HEADER_TOP_OFFSET = 7 * mm

# -------------------- Helpers --------------------
def draw_bordered_rect(c, x, y, w, h):
    c.setStrokeColor(black)
    c.setLineWidth(BORDER_WIDTH)
    c.rect(x, y, w, h, stroke=1, fill=0)

def draw_text(c, text, x, y, size=LABEL_SIZE, color=black, align='left'):
    c.setFont('Helvetica', size)
    c.setFillColor(color)
    if align == 'left':
        c.drawString(x, y, text)
    elif align == 'center':
        c.drawCentredString(x, y, text)
    elif align == 'right':
        c.drawRightString(x, y, text)

def draw_header(c, text, x, y):
    draw_text(c, text, x, y, size=HEADER_SIZE, color=gray, align='left')

def add_text_field(c, name, x, y, width, height, multiline=False, font_size=10, default=""):
    flags = 4096 if multiline else 0
    c.acroForm.textfield(
        name=name,
        x=x,
        y=y,
        width=width,
        height=height,
        fontSize=font_size,
        fillColor=Color(1,1,1),
        borderColor=black,
        borderWidth=0.5,
        borderStyle='solid',
        forceBorder=False,
        fieldFlags=flags,
        value=default,
    )

# -------------------- Page 1 --------------------
def page1(c):
    # ---- Identity bar ----
    id_y = H - MARGIN
    id_h = 0.08 * H
    id_x = MARGIN
    id_w = W - 2 * MARGIN
    draw_bordered_rect(c, id_x, id_y - id_h, id_w, id_h)

    id_labels = ['Race', 'Level', 'Name', 'Player']
    gap = id_w / len(id_labels)
    label_y = id_y - 8 * mm
    field_y = label_y - FIELD_HEIGHT - 2 * mm

    for i, label in enumerate(id_labels):
        x_center = id_x + (i + 0.5) * gap
        draw_text(c, label, x_center - 20*mm, label_y, align='center')
        fw = 50 * mm
        fx = x_center - fw/2
        add_text_field(c, f"field_{label}", fx, field_y, fw, FIELD_HEIGHT)

    # ---- Main body ----
    body_top = id_y - id_h - GUTTER
    body_bottom = MARGIN
    body_h = body_top - body_bottom

    col1_w = 0.26 * (W - 2 * MARGIN - GUTTER)
    col2_w = (W - 2 * MARGIN - GUTTER) - col1_w
    col1_x = MARGIN
    col2_x = col1_x + col1_w + GUTTER

    # ---- LEFT COLUMN ----
    # Attributes
    attr_h = 0.28 * body_h
    attr_y = body_top - attr_h
    draw_bordered_rect(c, col1_x, attr_y, col1_w, attr_h)
    draw_header(c, 'Attributes', col1_x + 4*mm, attr_y + attr_h - HEADER_TOP_OFFSET)

    attr_names = ['Might', 'Insight', 'Grace', 'Resolve', 'Vitality', 'Presence']

    max_label_len = max(len(name) for name in attr_names)
    col_width = (max_label_len * 4.5 * mm) + 6 * mm  

    total_group_width = 2 * col_width + GUTTER
    if total_group_width > col1_w - 8*mm:
        col_width = (col1_w - 8*mm - GUTTER) / 2
        total_group_width = 2 * col_width + GUTTER
    start_x = col1_x + (col1_w - total_group_width) / 2

    field_width = col_width - 2*mm
    row_height = (attr_h - 18*mm) / 3
    for i, name in enumerate(attr_names):
        col = 0 if i < 3 else 1
        row = i % 3
        x_label = start_x + col * (col_width + GUTTER)
        y_label = attr_y + attr_h - 12*mm - row * row_height
        draw_text(c, name, x_label, y_label, size=10)
        field_x = x_label
        field_y = y_label - FIELD_HEIGHT - 1*mm
        add_text_field(c, f"field_attr_{name}", field_x, field_y, field_width, FIELD_HEIGHT)

    # Conditions
    cond_h = 0.15 * body_h
    cond_y = body_bottom
    draw_bordered_rect(c, col1_x, cond_y, col1_w, cond_h)
    draw_header(c, 'Conditions', col1_x + 4*mm, cond_y + cond_h - HEADER_TOP_OFFSET)
    cond_field_x = col1_x + 4*mm
    cond_field_y = cond_y + 4*mm
    cond_field_w = col1_w - 8*mm
    cond_field_h = cond_h - 14*mm
    add_text_field(c, "field_conditions", cond_field_x, cond_field_y, cond_field_w, cond_field_h, multiline=True)

    # Skills
    skills_top = attr_y - GUTTER
    skills_bottom = cond_y + cond_h + GUTTER
    skills_h = skills_top - skills_bottom
    draw_bordered_rect(c, col1_x, skills_bottom, col1_w, skills_h)
    draw_header(c, 'Skills', col1_x + 4*mm, skills_bottom + skills_h - HEADER_TOP_OFFSET)

    skill_list = [
        ('Athletics', '(Might)'),
        ('Crafting', '(Gr/Ins)'),
        ('Deft Hands', '(Grace)'),
        ('Endurance', '(Vitality)'),
        ('Intimidation', '(Might/Pres)'),
        ('Intuition', '(Insight/Res)'),
        ('Investigation', '(Insight/Res)'),
        ('Medicine', '(Insight)'),
        ('Negotiation', '(Pres/Ins)'),
        ('Perception', '(Insight)'),
        ('Performance', '(Presence)'),
        ('Stealth', '(Grace)'),
        ('Survival', '(Ins/Res)')
    ]
    skill_step = (skills_h - 14*mm) / len(skill_list)
    skill_field_w = 25 * mm
    for idx, (skill, tag) in enumerate(skill_list):
        y_base = skills_bottom + skills_h - 14*mm - idx * skill_step
        draw_text(c, skill, col1_x + 4*mm, y_base, size=9)
        draw_text(c, tag, col1_x + 4*mm, y_base - 4*mm, size=8, color=gray)
        field_x = col1_x + col1_w - skill_field_w - 4*mm
        field_y = y_base - FIELD_HEIGHT/2 - 1*mm
        add_text_field(c, f"field_skill_{skill.replace(' ', '_')}", field_x, field_y, skill_field_w, FIELD_HEIGHT)

    # ---- RIGHT COLUMN ----
    # Health & Defense 
    health_h = 0.18 * body_h
    health_y = body_top - health_h
    draw_bordered_rect(c, col2_x, health_y, col2_w, health_h)
    draw_header(c, 'Health & Defense', col2_x + 4*mm, health_y + health_h - HEADER_TOP_OFFSET)

    scale = 1.25
    gap_between = 2 * mm
    start_x = col2_x + 4 * mm
    available_width = col2_w - 8 * mm

    row1_base = [
        ('Vigor', 30*mm),
        ('Aether', 30*mm),
        ('Poise', 30*mm),
        ('Evasion', 20*mm),
    ]
    row2_base = [
        ('Physical', 15*mm),
        ('Fire', 15*mm),
        ('Holy', 15*mm),
        ('Lightning', 15*mm),
        ('Magic', 15*mm),
        ('B.Vigor',15*mm),
        ('B.Aether',15*mm),
    ]

    def get_scaled_items(row_base, scale, gap, available):
        items = []
        total_width = 0
        for label, base_w in row_base:
            w = base_w * scale
            items.append((label, w))
            total_width += w
        total_width += (len(items)-1) * gap
        if total_width > available:

            extra = total_width - available
            reduction = min(extra / (len(items)-1), gap * 0.9)
            new_gap = gap - reduction
            return items, new_gap
        else:
            return items, gap

    row1_items, gap1 = get_scaled_items(row1_base, scale, gap_between, available_width)
    row2_items, gap2 = get_scaled_items(row2_base, scale, gap_between, available_width)

    y_row1_label = health_y + health_h - 12*mm
    y_row1_field = y_row1_label - FIELD_HEIGHT - 1*mm
    x = start_x
    for label, width in row1_items:
        if label != "Evasion":
            draw_text(c, label, x+width/7, y_row1_label, align='center', size=10)
        else:
            draw_text(c, label, x+width/4, y_row1_label, align='center', size=10)
        add_text_field(c, f"field_health_{label}", x, y_row1_field, width, FIELD_HEIGHT)
        x += width + gap1

    y_row2_label = health_y + health_h - 28*mm
    x = start_x
    draw_text(c, 'DR Values:', x+11*mm, y_row2_label, align='center', size=12, color=gray)
    x= start_x 
    y_row2_label = health_y + health_h - 31*mm
    y_row2_field = y_row2_label - FIELD_HEIGHT - 1*mm
    for label, width in row2_items:
        if  label == "Physical":
            draw_text(c, label, x + 8*mm, y_row2_label, align='center', size=10)
        elif label == "Lightning":
            draw_text(c, label, x + 8*mm, y_row2_label, align='center', size=10)
        elif label == "Magic":
            draw_text(c, label, x + 5*mm, y_row2_label, align='center', size=10)
        elif label == "B.Vigor":
            draw_text(c, label, x + 6*mm, y_row2_label, align='center', size=10)
            draw_text(c, "Base Values:", x + 12*mm, y_row2_label+3*mm, align='center', size=12, color=gray)
        elif label == "B.Aether":
             draw_text(c, label, x + 7*mm, y_row2_label, align='center', size=10)
        else:
            draw_text(c, label, x + 4*mm, y_row2_label, align='center', size=10)
        add_text_field(c, f"field_health_{label.replace(' ', '_')}", x, y_row2_field, width, FIELD_HEIGHT)
        x += width + gap2

    # ---- Middle row: Travel Rate + Status ----
    middle_h = 0.30 * body_h
    middle_y = health_y - GUTTER - middle_h
    travel_w = 0.30 * col2_w
    draw_bordered_rect(c, col2_x, middle_y, travel_w, middle_h)
    draw_header(c, 'Travel Rate', col2_x + 4*mm, middle_y + middle_h - HEADER_TOP_OFFSET)
    travel_field_x = col2_x + 4*mm
    travel_field_y = middle_y + 4*mm
    travel_field_w = travel_w - 8*mm
    travel_field_h = middle_h - 14*mm
    add_text_field(c, "field_travel_rate", travel_field_x, travel_field_y, travel_field_w, travel_field_h, multiline=True)

    # Status Effects (table: status name + buildup/resistance fields)
    stat_x = col2_x + travel_w + GUTTER
    stat_w = col2_w - travel_w - GUTTER
    draw_bordered_rect(c, stat_x, middle_y, stat_w, middle_h)
    draw_header(c, 'Status Effect', stat_x + 4*mm, middle_y + middle_h - HEADER_TOP_OFFSET)

    status_list = ['Bleed', 'Frostbite', 'Sleep', 'Poison', 'Scarlet Rot', 'Madness', 'Deathblight']
    status_step = (middle_h - 14*mm) / len(status_list)
    status_field_w = (stat_w - 8*mm - 22*mm - 2*mm) / 2  # buildup + resistance either side of a 2mm gutter
    status_field_h = min(FIELD_HEIGHT, status_step - 2*mm)
    # Add buildup and resistance value label on top of the fields
    build_x = stat_x + stat_w - 2*status_field_w - 6*mm
    resist_x = build_x + status_field_w + 2*mm
    draw_text(c,"Build Up", build_x + status_field_w/3, middle_y + middle_h - 12*mm, size=10)
    draw_text(c,"Res Value", resist_x + status_field_w/3 -2*mm, middle_y + middle_h - 12*mm, size=10)
    for idx, status in enumerate(status_list):
        y_base = middle_y + middle_h - 16*mm - idx * status_step 
        field_y = y_base - status_field_h/2 - 1*mm
        draw_text(c, status, stat_x + 4*mm, field_y + status_field_h/2 - 1.5*mm, size=9)
        add_text_field(c, f"field_status_{status.replace(' ', '_')}_buildup", build_x, field_y, status_field_w, status_field_h)
        add_text_field(c, f"field_status_{status.replace(' ', '_')}_resist", resist_x, field_y, status_field_w, status_field_h)

    # ---- Abilities & Actions ----
    abil_y = body_bottom
    abil_h = middle_y - GUTTER - body_bottom
    draw_bordered_rect(c, col2_x, abil_y, col2_w, abil_h)
    draw_header(c, 'Abilities & Actions', col2_x + 4*mm, abil_y + abil_h - HEADER_TOP_OFFSET)
    abil_field_x = col2_x + 4*mm
    abil_field_y = abil_y + 4*mm
    abil_field_w = col2_w - 8*mm
    abil_field_h = abil_h - 14*mm
    add_text_field(c, "field_abilities", abil_field_x, abil_field_y, abil_field_w, abil_field_h, multiline=True)

# -------------------- Page 2 --------------------
def page2(c):
    tracker_h = 0.39 * H
    tracker_y = H - MARGIN - tracker_h
    draw_bordered_rect(c, MARGIN, tracker_y, W - 2*MARGIN, tracker_h)
    draw_header(c, 'Character Tracker', MARGIN + 4*mm, tracker_y + tracker_h - HEADER_TOP_OFFSET)
    top_labels = ['Spare Trait Points', 'Languages']
    num_slots = 5
    gap = (W - 2*MARGIN) / num_slots
    y_label = tracker_y + tracker_h - 16*mm
    y_field = y_label - FIELD_HEIGHT - 2*mm

    for i, label in enumerate(top_labels):
        x_center = MARGIN + (i + 0.5) * gap
        draw_text(c, label, x_center-4*mm, y_label, align='center', size=10)
        if label == 'Spare Trait Points':
            fw = 36*mm
            fx = x_center - fw/2 + 2*mm
            add_text_field(c, f"field_{label.replace(' ', '_')}", fx - 2*mm, y_field, fw, FIELD_HEIGHT)
            souls_x = fx + 4*mm
            souls_y_base = y_field - FIELD_HEIGHT - 2*mm
        else:
            fw = 37*mm
            fh = 32*mm
            add_text_field(c, f"field_{label.replace(' ', '_')}", x_center - fw/2, y_field - 22*mm, fw, fh, multiline=True)

    # Souls (was Gilded Mints)
    draw_text(c, 'Souls', souls_x - 6*mm, souls_y_base + 2*mm, size=10)
    souls_field_y = souls_y_base - FIELD_HEIGHT
    add_text_field(c, "field_Souls", souls_x - 6*mm, souls_field_y, 36*mm, FIELD_HEIGHT)

    # Talisman (reclaimed space from Faith / old Languages / Alt investments slots)
    tal_x = MARGIN + 2 * gap
    tal_w = 3 * gap - 4*mm
    tal_top = y_label + 4*mm
    tal_bottom = y_field - 22*mm
    tal_h = tal_top - tal_bottom
    draw_bordered_rect(c, tal_x, tal_bottom, tal_w, tal_h)
    draw_text(c, 'Talisman', tal_x + 4*mm, tal_top - 6*mm, size=11, color=gray)

    tal_gutter = 1*mm
    tal_field_w = tal_w - 8*mm
    tal_field_h = (tal_h - 10*mm - 2*tal_gutter) / 3
    for i in range(3):
        fy = (tal_bottom + 3*mm) + i * (tal_field_h + tal_gutter)
        add_text_field(c, f"field_Talisman_{i+1}", tal_x + 4*mm, fy, tal_field_w, tal_field_h, multiline=True)

    # Inventory 
    inv_y = souls_field_y - FIELD_HEIGHT 
    draw_text(c, 'Inventory', MARGIN + 2*mm, inv_y+2*mm, size=10)
    inv_h = tracker_y + tracker_h - inv_y - 4*mm
    add_text_field(c, "field_Inventory", MARGIN + 2*mm, inv_y - inv_h + 4*mm, W - 2*MARGIN - 4*mm, inv_h - 4 *mm, multiline=True)


    # Backstory
    backstory_y = MARGIN
    backstory_h = tracker_y - MARGIN - GUTTER
    draw_bordered_rect(c, MARGIN, backstory_y, W - 2*MARGIN, backstory_h)
    draw_header(c, 'Backstory', MARGIN + 4*mm, backstory_y + backstory_h - HEADER_TOP_OFFSET)
    bs_x = MARGIN + 4*mm
    bs_y = backstory_y + 4*mm
    bs_w = W - 2*MARGIN - 8*mm
    bs_h = backstory_h - 14*mm
    add_text_field(c, "field_Backstory", bs_x, bs_y, bs_w, bs_h, multiline=True)

# -------------------- Main --------------------
def main():
    pdf_file = 'Character_Sheet_Ash&Souls.pdf'
    c = canvas.Canvas(pdf_file, pagesize=A4)
    page1(c)
    c.showPage()
    page2(c)
    c.showPage()
    c.save()
    print(f'✅ PDF created: {pdf_file}')

if __name__ == '__main__':
    main()
