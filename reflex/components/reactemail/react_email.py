from types import ClassMethodDescriptorType
import reflex as rx 
from reflex.components.radix.themes.typography.text import text
from reflex.utils.compat import windows_hot_reload_lifespan_hack
from reflex.utils.types import Optional
from reflex.vars.base import Var

class EmailComponent(rx.Component):
    library = "@react-email/components"

class Html(EmailComponent):
    """Html component for email content"""
    tag = "Html"
    lang: rx.Var[str]
    dir: rx.Var[str]

    @classmethod
    def create(cls, *children, **props):
        """
        Create the Html component.

        Args:
            *children: The child elements for the Html tag.
            **props: Properties such as `lang`, `dir`, and any custom styles.

        Returns:
            Html component.
        """
        return super().create(*children, **props)

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
    """Link component for email content"""
    tag = "Link"
    href: Var[str]
    target: Var[str]
    text: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """
        Create a Link component.

        Args:
            *children: The text or elements to display as the link content.
            **props: Properties such as 'href', 'target', and styles for customizing the appearance of the link.

        Returns:
            A Link component with a clickable URL.
        """
        if 'text' in props:
            children = [props.pop('text')]
        props['href'] = Var.create(props.get('href', '#'))
        props['target'] = Var.create(props.get('target', '_blank'))
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)

class Text(EmailComponent):
    """Text component for email content"""
    tag = "Text"

    @classmethod
    def create(cls, *children, **props):

        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])

        return super().create(*children, **props)


class Image(EmailComponent):
    """Image component for rendering images in email content."""
    tag = "Img"
    alt: Var[str]
    src: Var[str]
    width: Var[str]
    height: Var[str]

    @classmethod
    def create(cls, *children, **props):
        """
        Create an Image component.

        Args:
            *children: Optional child components to render alongside the image.
            **props: Properties such as 'src', 'alt', 'width', 'height', and 'style' for customizing the image.

        Returns:
            An Image component for embedding pictures in emails.
        """
        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)

class Head(EmailComponent):
    """Head componet for email content"""
    tag="Head"

class Container(EmailComponent):
    """Container component for wrapping and aligning multiple components."""
    tag="Container"


    @classmethod
    def create(cls, *children, **props):
        """
        Create a Container component.

        Args:
            *children: Child components to wrap inside the container.
            **props: Additional properties like 'style' for customizing layout, padding, and alignment.

        Returns:
            A Container component for organizing content.
        """
        #style handle
        if 'style' in props:
            props['style'] = Var.create(props['style'])
        return super().create(*children, **props)

class Hr(EmailComponent):
    """Hr component for adding horizontal dividers in the email"""
    tag="Hr"
    @classmethod
    def create(cls, *children, **props):
        """
        Create a Hr component.

        Args:
            *children: Optional child components, though usually none are used for this component.
            **props: Properties for customizing the appearance of the horizontal line, like 'style'.

        Returns:
            A Hr component to create a horizontal rule in the email content.
        """
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

