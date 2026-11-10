-- Paperback rules: perldoc/MetaCPAN links dropped (and indexed); other links
-- footnoted unless the link text is the URL; unnumbered chapters set running heads.
local function norm(u) return (u:gsub('/$','')) end
function Link(el)
  local t = el.target
  local f = t:match('^https://perldoc%.perl%.org/functions/(.+)$')
  if f then
    return {el.content[1], pandoc.RawInline('latex', '\\index{' .. f .. '@\\texttt{' .. f .. '()}}')}
  end
  local m = t:match('^https://metacpan%.org/pod/(.+)$')
  if m then
    return {pandoc.Span(el.content), pandoc.RawInline('latex', '\\index{' .. m .. '}')}
  end
  if t:sub(1,1) == '#' then return el.content end
  if norm(pandoc.utils.stringify(el.content)) == norm(t) then
    return pandoc.RawInline('latex', '\\url{' .. pandoc.utils.stringify(el.content) .. '}')
  end
  local out = el.content
  out:insert(pandoc.Note({pandoc.Plain({pandoc.RawInline('latex', '\\url{' .. t .. '}')})}))
  return out
end
function Header(el)
  if el.level == 1 and el.classes:includes('unnumbered') then
    local s = pandoc.utils.stringify(el)
    return {el, pandoc.RawBlock('latex', '\\markboth{' .. s .. '}{' .. s .. '}')}
  end
end
function Code(el)
  if el.text:match('_') and el.text:match('^[%w_%$@%%]+$') then
    local s = el.text:gsub('%$','\\$'):gsub('%%','\\%%'):gsub('_','\\_\\allowbreak{}')
    return pandoc.RawInline('latex', '\\texttt{' .. s .. '}')
  end
end
