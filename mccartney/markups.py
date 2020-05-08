"""
markup library
"""
import typing 

import abjad

### FACTORY FUNCTIONS ###

def instrument(
    string: typing.Union[str, typing.List[str]],
    hcenter_in: typing.Optional[abjad.Number] = 16,
    column: bool = True,
) -> abjad.Markup:
    r"""
    Makes instrument name markup.
    ..  container:: example
        Makes instrument name markup in column:
        >>> markup = baca.markups.instrument('Eng. horn')
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \hcenter-in
                    #16
                    "Eng. horn"
                }
    ..  container:: example
        Makes instrument name markup in line:
        >>> markup = baca.markups.instrument(
        ...     'Violin 1',
        ...     column=False,
        ...     )
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \hcenter-in
                    #16
                    "Violin 1"
                }
    Centers markup horizontally in 16 spaces.
    """
    return make_instrument_name_markup(string, column=column, hcenter_in=hcenter_in)

def short_instrument(
    string: str, hcenter_in: abjad.Number = 10, column: bool = True
) -> abjad.Markup:
    r"""
    Makes short instrument name markup.
    ..  container:: example
        Makes short instrument name markup in column:
        >>> markup = baca.markups.short_instrument('Eng. hn.')
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \hcenter-in
                    #10
                    "Eng. hn."
                }
    ..  container:: example
        Makes short instrument name markup in line:
        >>> markup = baca.markups.short_instrument(
        ...     'Vn. 1',
        ...     column=False,
        ...     )
        >>> abjad.show(markup, strict=89) # doctest: +SKIP
        ..  docs::
            >>> abjad.f(markup, strict=89)
            \markup {
                \hcenter-in
                    #10
                    "Vn. 1"
                }
    Centers markup horizontally in 10 spaces.
    """
    return make_instrument_name_markup(string, column=column, hcenter_in=hcenter_in)
