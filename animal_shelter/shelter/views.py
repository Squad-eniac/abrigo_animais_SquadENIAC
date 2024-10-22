from django.shortcuts import render
from django.views.generic import ListView
from .models import Animal
from django.db.models import Q


class AnimalListView(ListView):
    model = Animal
    template_name = "animal_list.html"
    context_object_name = "animals"

    def get_queryset(self):
        queryset = Animal.objects.filter(enabled=True)

        # Filter by search query
        search_query = self.request.GET.get("search_term", "")
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
                | Q(breed__icontains=search_query)
                | Q(species__icontains=search_query)
                | Q(age__icontains=search_query)
                | Q(health_history__icontains=search_query),
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the search query in the context
        context["search_query"] = self.request.GET.get("search_term", "")
        return context
