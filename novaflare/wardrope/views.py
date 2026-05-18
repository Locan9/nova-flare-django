from django.shortcuts import render
from .models import SavedSubmission




class NovaFlareEngine:
    """
    NovaFlare Engine handles wardrobe input parsing, clothing combination logic,
    and complex item color matching matrices.
    """
    
    # 1. Class Attributes (Static rule definitions)
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
        """Initializes the instance and immediately parses the input."""
        self.raw_text = raw_text
        self.item_colors = self._parse_input()
        self.owned_items = list(self.item_colors.keys())

    def _parse_input(self):
        """Helper internal method to clean up and parse text lines."""
        lines = [line.strip() for line in self.raw_text.split('\n') if line.strip()]
        parsed_wardrobe = {}
        
        for line in lines:
            if ':' in line:
                item, colors = line.split(':', 1)
                color_list = [c.strip().lower() for c in colors.split(',')]
                parsed_wardrobe[item.strip().lower()] = color_list
                
        return parsed_wardrobe

    def get_recommendations(self):
        """Processes combinations and executes the color compatibility matching matrix."""
        recommendation_results = []
        recommended_outfits = []

        # Find base outfits matching owned items
        for outfit in self.OUTFITS:
            if all(item in self.owned_items for item in outfit):
                recommended_outfits.append(outfit)

        # Loop through matches
        for outfit in recommended_outfits:
            # Handle 2-Piece Combos
            if len(outfit) == 2:
                for c1 in self.item_colors[outfit[0]]:
                    for c2 in self.item_colors[outfit[1]]:
                        if c2 in self.COLOR_MATCH.get(c1, []):
                            msg = f"✨ {outfit[0].title()} ({c1}) + {outfit[1].title()} ({c2})"
                            recommendation_results.append(msg)

            # Handle 3-Piece Combos
            elif len(outfit) == 3:
                for c1 in self.item_colors[outfit[0]]:
                    for c2 in self.item_colors[outfit[1]]:
                        for c3 in self.item_colors[outfit[2]]:
                            if (c2 in self.COLOR_MATCH.get(c1, []) and
                                c3 in self.COLOR_MATCH.get(c1, []) and
                                c3 in self.COLOR_MATCH.get(c2, [])):
                                msg = f"🔥 {outfit[0].title()} ({c1}) + {outfit[1].title()} ({c2}) + {outfit[2].title()} ({c3})"
                                recommendation_results.append(msg)

        return recommendation_results


def index_view(request):
    """Simple index view: run engine on POST and render results.

    Also saves each submission (one SavedSubmission per POST) with the generated
    recommendations, associated with the current user if logged in or with the
    session key otherwise.
    """
    user_input = request.POST.get('user_input', '') if request.method == 'POST' else ''
    recommendations = NovaFlareEngine(user_input).get_recommendations() if user_input else []

    if request.method == 'POST' and recommendations:
        # store as HTML paragraphs so the saved page can display the same
        # `.match-text` paragraphs as the main page. We keep raw_input too.
        results_text = "".join([f"<p class=\"match-text\">{r}</p>" for r in recommendations])
        try:
            SavedSubmission.objects.create(
                user=(request.user if request.user.is_authenticated else None),
                raw_input=user_input,
                results=results_text,
            )
        except Exception:
            # don't break if save fails
            pass

    return render(request, 'index.html', {'recommendations': recommendations, 'user_input': user_input})


def saved_view(request):
    """Show saved submissions for the current user or session."""
    # If user is authenticated show their submissions; otherwise show recent submissions
    if request.user.is_authenticated:
        submissions = SavedSubmission.objects.filter(user=request.user)
    else:
        submissions = SavedSubmission.objects.all().order_by('-created_at')[:50]

    return render(request, 'saved.html', {'submissions': submissions})



