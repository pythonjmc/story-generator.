import random
stories = ["This is a morality tale. The story is about an unconfident inventor whose species is being exterminated. It takes place in an interplanetary syndicate. The story begins with a resignation. The end of one era and the beginning of another is a major element of the story.",
    "The story is about a teacher who seems insane. It takes place in a galaxy of magic. The story begins with an addiction, climaxes with a critical injury, and ends with someone borrowing money.",
    "This is a natural disaster with a strong theme of pursuit and the need for change and growth. The story is about a daycare employee. It starts in a smithy in a small town. The crux of the story involves the making of a meal.",
    "This is a tale about deceit and how people are a lot alike. The story is about a merchant who must work with an industrious servant. It starts in a tourist town on a swamp planet. An ancient evil coming back to life is a major part of the story.",
    "The story is about a veterinarian and a fearful traitor. It starts in a library. The story climaxes with somebody breaking something important. The side effects of faster-than-light travel play a major role in the story.",
    "This is an epic about jealousy. The story is about a chaste daycare employee who is in debt to a cyberpunk. It starts in a university. The story begins with an illness, climaxes with a delusion, and ends with the preparation for a performance. The return of an ancient evil plays an important part in the story.",
    "This is an epic drama. The story is about a starship pilot who is best friends with a hermit. It starts in a farm. The spread of new diseases in a global age plays a major part in this story.",
    "The story is about a spy who was once married to a pious car salesman. It takes place in a bakery in a metropolis. The story begins with the revelation of a dark secret and ends with a keepsake. Weapons proliferation plays a major role in this story.",
    "The story is about an outlaw who is mysteriously connected to a librarian. It starts on a world of magic. The story climaxes with a natural disaster.",
    "This is a psychological revelation piece with an emphasis on how life is a tragedy. The story is about a nuclear engineer. It takes place aboard a medical starship. The generation gap plays a major part in this story."
]

def get_story():
    return random.choice(stories)
