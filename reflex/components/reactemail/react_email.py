from types import ClassMethodDescriptorType
import reflex as rx 
from reflex.components.radix.themes.typography.text import text
from reflex.utils.compat import windows_hot_reload_lifespan_hack
from reflex.utils.types import Optional
from reflex.vars.base import Var

class EmailComponent(rx.Component):
    library = "@react-email/components"

class Html(EmailComponent):
    tag = "Html"
    lang: rx.Var[str]
    dir: rx.Var[str]

class Button(EmailComponent):
    tag = "Button"
    href: Var[str]
    target: Var[str]
    text: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """Create the Link component.

        Args:
            *children: The children components or elements (e.g., text).
            **props: Props such as `href` and `target`.

        Returns:
            Link component with provided props and children.
        """
        #Handle the text prop by converting it to children if present
        if 'text' in props:
            children = [props.pop('text')]
           #props.pop('text') #no need of text as prop
        # Ensure the 'href' prop is passed
        props['href'] = Var.create(props.get('href', '#'))
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        props['target'] = Var.create(props.get('target', '_blank'))

        # If there is text in the children, use it as the link's content
        return super().create(*children, **props)

class Link(EmailComponent):
    tag = "Link"
    href: Var[str]
    target: Var[str]
    text: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """Create the Link component.

        Args:
            *children: The children components or elements (e.g., text).
            **props: Props such as `href` and `target`.

        Returns:
            Link component with provided props and children.
        """
        #Handle the text prop by converting it to children if present
        if 'text' in props:
            children = [props.pop('text')]
           #props.pop('text') #no need of text as prop
        # Ensure the 'href' prop is passed
        props['href'] = Var.create(props.get('href', '#'))
        props['target'] = Var.create(props.get('target', '_blank'))
        #props['style'] = Var.create(props['style'])

        # If there is text in the children, use it as the link's content
        return super().create(*children, **props)

class Text(EmailComponent):
    tag = "Text"

    @classmethod
    def create(cls, *children, **props):
        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])

        return super().create(*children, **props)


class Image(EmailComponent):
    tag = "Img"
    alt: Var[str]
    src: Var[str]
    width: Var[str]
    height: Var[str]

    @classmethod
    def create(cls, *children, **props):
        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)

class Head(EmailComponent):
    tag="Head"

class Container(EmailComponent):
    tag="Container"


    @classmethod
    def create(cls, *children, **props):
        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)

class Hr(EmailComponent):
    tag="Hr"
    @classmethod
    def create(cls, *children, **props):
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)


class Heading(EmailComponent):
    """Wrapper for the React-Email Heading component."""

    tag = "Heading"
    as_: Var[str] 
    m: Var[str] 
    mx: Var[str] 
    my: Var[str] 
    mt: Var[str] 
    mr: Var[str] 
    mb: Var[str] 
    ml: Var[str] 
    text: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """Create the Heading component.

        Args:
            *children: Children components or elements.
            **props: Props such as `as_`, `m`, `mx`, `my`, etc.

        Returns:
            Heading component with provided props and children.
        """
        # Convert 'as_' to 'as' for the props dictionary
        if 'as_' in props:
            props['as'] = props.pop('as_')
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        # Handle the text prop by converting it to children if present
        if 'text' in props:
            children = [props.pop('text')]

        return super().create(*children, **props)

