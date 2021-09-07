from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

# Create your views here.
from subscriptions import views, forms
from .forms import CustomPaymentForm
from robokassa.forms import RobokassaForm

# Override template of SubscribeView

@login_required
def pay_with_robokassa(request):

    form = RobokassaForm(initial={
               'OutSum': 100,
               'InvId': 123,
               'Desc': 'test',
               'Email': 'go.go.nest.nest@gmail.com',
               # 'IncCurrLabel': '',
               # 'Culture': 'ru'
           })

    return render(request, 'subscription_page/pay_with_robokassa.html', {'form': form})

# class CustomSubscribeView(views.SubscribeView):
#     #payment_form = CustomPaymentForm
    

#     def render_preview(self, request, **kwargs):
#         """Renders preview of subscription and collect payment details."""
#         self.confirmation = False
#         context = self.get_context_data(**kwargs)

#         # Forms to collect subscription details
#         if 'error' in kwargs:
#             plan_cost_form = forms.SubscriptionPlanCostForm(
#                 request.POST, subscription_plan=self.subscription_plan
#             )
#             payment_form = RobokassaForm(request.POST)
#         else:
#             plan_cost_form = forms.SubscriptionPlanCostForm(
#                 initial=request.POST, subscription_plan=self.subscription_plan
#             )
#             payment_form = RobokassaForm(initial=request.POST)

#         context['plan_cost_form'] = plan_cost_form
#         context['payment_form'] = payment_form

#         return self.render_to_response(context)
    
#     def render_confirmation(self, request, **kwargs):
#         """Renders a confirmation page before processing payment.

#             If forms are invalid will return to preview view for user
#             to correct errors.
#         """
#         # Retrive form details
#         plan_cost_form = forms.SubscriptionPlanCostForm(
#             request.POST, subscription_plan=self.subscription_plan
#         )
#         payment_form = RobokassaForm(request.POST)

#         # Validate form submission
#         if all([payment_form.is_valid(), plan_cost_form.is_valid()]):
#             self.confirmation = True
#             context = self.get_context_data(**kwargs)

#             # Forms to process payment (hidden to prevent editing)
#             context['plan_cost_form'] = self.hide_form(plan_cost_form)
#             context['payment_form'] = self.hide_form(payment_form)

#             # Add the PlanCost instance to context for use in template
#             context['plan_cost'] = plan_cost_form.cleaned_data['plan_cost']

#             return self.render_to_response(context)

#         # Invalid form submission - render preview again
#         kwargs['error'] = True
#         return self.render_preview(request, **kwargs)

    