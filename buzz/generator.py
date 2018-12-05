import random

buzz = (
    'continuous testing',
    'continuous integration',
    'continuous deployment',
    'continuous improvement',
    'continuous fasting',
    'devops',
)
adjectives = (
    'complete',
    'modern',
    'self-service',
    'integrated',
    'end-to-end',
    'disruptive'
)
adverbs = (
    'remarkably',
    'enormously',
    'substantially',
    'significantly',
    'seriously',
    'gracefully'
)
verbs = (
    'accelerates',
    'improves',
    'enhances',
    'revamps',
    'boosts',
)

def sample(samples, k=1):
    result = random.sample(samples, k)
    if k == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([
        sample(adjectives),
        buzz_terms[0],
        sample(adverbs),
        sample(verbs),
        buzz_terms[1]    
    ])
    return phrase.title()

def main():
    print(generate_buzz())

if __name__ == '__main__':
    print(generate_buzz())