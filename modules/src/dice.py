import random

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6'
}


def process(input, entities=None):
    message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
    message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
    message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
