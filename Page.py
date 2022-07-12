from robot.libraries.BuiltIn import BuiltIn

def chain_selectors(selectorList, **formatters):
  return ' >> '.join(selectorList).format(**formatters)

_locators = {
  'activeView': 'div.maincontent div.oneContent.active',
  'form': 'form[name="{formName}"]',
  'field': '.slds-form-element:has(.slds-form-element__label:text-is("{fieldName}"),.slds-form-element__label :text-is("{fieldName}")) .slds-form-element__control',
  'input': 'input',
  'textarea': 'textarea',
  'selectedOption': 'option:checked'
}

class Page:
  def __init__(self):
    self.builtin = BuiltIn()

  @property
  def browser(self):
    return self.builtin.get_library_instance('Browser')

  def get_field_value(self, fieldName):
    selector = chain_selectors([_locators['activeView'], _locators['field'], f"{_locators['input']},{_locators['textarea']},{_locators['selectedOption']}"], fieldName=fieldName)
    self.builtin.log_to_console(f'\n{fieldName} selector: {selector}')
    element = self.browser.get_element(selector)
    states = self.browser.get_element_states(element)
    self.builtin.log_to_console(f'\n{fieldName} states: {states}')

    return self.browser.get_text(element)
