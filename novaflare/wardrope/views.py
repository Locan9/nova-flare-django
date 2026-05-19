from django.shortcuts import render
from .models import SavedSubmission




class NovaFlareEngine:
   
    
    
    OUTFITS = [
        ["tshirt", "jeans"], ["tshirt", "sweatpants"], ["tshirt", "shorts"],
        ["hoodie", "jeans"], ["hoodie", "sweatpants"],
        ["casual shirt", "jeans"], ["casual shirt", "pants"],
        ["light jacket", "casual shirt", "jeans"],
        ["light jacket", "casual shirt", "sweatpants"],
        ["light jacket", "hoodie", "sweatpants"],
        ["light jacket", "hoodie", "jeans"]
    ]

    ALL_COLORS = [
        "light green", "dark green", "light blue", "dark blue",
        "light yellow", "dark yellow", "black", "white",
        "light red", "dark red", "light orange", "dark orange",
        "light purple", "dark purple", "light brown", "dark brown", "silver"
    ]

    COLOR_MATCH = {
        "black": ALL_COLORS, "white": ALL_COLORS,
        "light blue": ["white", "black", "dark blue", "light brown", "silver"],
        "dark blue": ["white", "light blue", "black", "dark brown", "silver"],
        "light green": ["white", "black", "light brown"],
        "dark green": ["white", "black", "dark brown"],
        "light red": ["white", "black", "light blue"],
        "dark red": ["white", "black", "dark blue"],
        "light yellow": ["black", "white", "dark blue"],
        "dark yellow": ["black", "dark brown"],
        "light orange": ["white", "dark blue"],
        "dark orange": ["black", "dark brown"],
        "light purple": ["white", "black", "light blue"],
        "dark purple": ["white", "black"],
        "light brown": ["white", "black", "light green"],
        "dark brown": ["white", "light blue", "black"],
        "silver": ["black", "white", "light blue", "dark blue"]
    }

    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.item_colors = self._parse_input()
        self.owned_items = list(self.item_colors.keys())

    def _parse_input(self):
    
        lines = [line.strip() for line in self.raw_text.split('\n') if line.strip()]
        parsed_wardrobe = {}
        
        for line in lines:
            if ':' in line:
                item, colors = line.split(':', 1)
                color_list = [c.strip().lower() for c in colors.split(',')]
                parsed_wardrobe[item.strip().lower()] = color_list
                
        return parsed_wardrobe

    def get_recommendations(self):
        
        recommendation_results = []
        recommended_outfits = []

       
        for outfit in self.OUTFITS:
            if all(item in self.owned_items for item in outfit):
                recommended_outfits.append(outfit)

       
        for outfit in recommended_outfits:
            # Handle 2-Piece Combos
            if len(outfit) == 2:
                for c1 in self.item_colors[outfit[0]]:
                    for c2 in self.item_colors[outfit[1]]:
                        if c2 in self.COLOR_MATCH.get(c1, []):
                            msg = f" {outfit[0].title()} ({c1}) + {outfit[1].title()} ({c2})"
                            recommendation_results.append(msg)

            # Handle 3-Piece Combos
            elif len(outfit) == 3:
                for c1 in self.item_colors[outfit[0]]:
                    for c2 in self.item_colors[outfit[1]]:
                        for c3 in self.item_colors[outfit[2]]:
                            if (c2 in self.COLOR_MATCH.get(c1, []) and
                                c3 in self.COLOR_MATCH.get(c1, []) and
                                c3 in self.COLOR_MATCH.get(c2, [])):
                                msg = f" {outfit[0].title()} ({c1}) + {outfit[1].title()} ({c2}) + {outfit[2].title()} ({c3})"
                                recommendation_results.append(msg)

        return recommendation_results


def index_view(request):
    recommendations = []
    user_input = ""

    if request.method == 'POST':
        user_input = request.POST.get('user_input', '').strip()
        if user_input:
            recommendations = NovaFlareEngine(user_input).get_recommendations()
            results_string = recommendations
            SavedSubmission.objects.create(
                raw_input=user_input,
                results=results_string
            )

    return render(request, 'index.html', {
        'recommendations': recommendations, 
        'user_input': user_input
    })


def saved_view(request):
    submissions = SavedSubmission.objects.all().order_by('-created_at')
    for sub in submissions:
        sub.list_of_results = eval(sub.results)
    return render(request, 'saved.html', {'submissions': submissions})



