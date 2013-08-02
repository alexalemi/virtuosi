-- Disable backslash escaping of special characters when writing strings to markdown.
import Text.Pandoc

main = toJsonFilter unescape
  where unescape (Str xs) = RawInline "markdown" xs
        unescape x        = x
