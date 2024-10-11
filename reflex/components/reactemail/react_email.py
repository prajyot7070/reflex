

from typing import Any, List

from reflex.components import Component
from reflex.vars import Var, LiteralVar
from reflex.utils.types import is_dataframe


class EmailComponent(Component):
    """Base class for React Email components."""
    library = "@react-email/components"


class Html(EmailComponent):
    """Wrapper for the React-Email Html component."""
    
    tag = "Html"
    lang: Var[str]
    dir: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """Create the Html component.

        Args:
            *children: Children components or elements.
            **props: Props such as `lang` and `dir`.

        Returns:
            Html component with provided props and children.
        """
        # Handle lang and dir props if passed in
        if 'lang' in props:
            props['lang'] = Var.create(props['lang'])
        if 'dir' in props:
            props['dir'] = Var.create(props['dir'])

        # Ensure children are properly handled
        props['children'] = children if children else []

        return super().create(**props)


class Button(EmailComponent):
    """Wrapper for the React-Email Button component."""
    
    tag = "Button"
    href: Var[str]
    target: Var[str]
    text: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """Create the Button component.

        Args:
            *children: Children components or elements.
            **props: Props such as `href`, `target`, and `text`.

        Returns:
            Button component with provided props and children.
        """
        # Check for required href prop
        if 'href' not in props:
            raise ValueError("The 'href' prop is required.")

        # Set href and target, with default values if not provided
        props['href'] = Var.create(props['href'])
        props['target'] = Var.create(props.get('target', '_blank'))
        #children = props['text']
        # Set text to children if provided, or leave it as an empty list
        text = props.pop('text', None)
        print(f"Creating Button with href: {props['href']}, text: {text}")

        if text is not None:
            props['children'] = [text]  # Set text as the visible button label
        else:
            props['children'] = children  # If no text is provided, use any existing children  # Use text as the button label

        # Assign children to props
        #props['children'] = children if children else []

        return super().create(**props)




