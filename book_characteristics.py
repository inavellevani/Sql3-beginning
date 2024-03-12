import random as rd

names = ['Divine Comedy', 'Me, grandma, Iliko and Ilarion', 'Kukaracha', 'The Catcher in the Rye', 'Don Quixote',
         'Blood meridian', 'The Master and Margarita', 'A song of ice and fire', 'Misery', 'It']

pages = [rd.randint(1, 400) for _ in range(10)]

cover_types = [
    'Geometric Patterns',
    'Retro Illustration',
    'Surreal Collage',
    'Typographic Emphasis',
    'Abstract Watercolor',
    'Cyberpunk Aesthetics',
    'Noir Photography',
    'Botanical Elegance',
    'Pop Art Explosion',
    'Monochromatic Minimalism'
]

categories = ['Epic poetry', 'Novel', 'Drama', 'First-person narrative', 'Satire',
              'Western', 'Fantasy', 'Fantasy Fiction', 'Thriller', 'Horror']