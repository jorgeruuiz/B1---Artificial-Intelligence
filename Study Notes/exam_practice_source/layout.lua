-- Keep a question and its options together; add writing space in mock PDFs.
function Pandoc(doc)
  if not FORMAT:match('latex') then return doc end
  doc.meta.lang = nil -- Use TeX's default English without an extra Babel language package.
  local out = pandoc.List()
  local open = false
  local short = false
  local short_count = 0
  local is_mock = pandoc.utils.stringify(doc.meta.title):match('Mock Papers') ~= nil
  local function close_question()
    if open then
      if is_mock and short then
        out:insert(pandoc.RawBlock('latex', '\\par\\vspace{28mm}'))
      end
      out:insert(pandoc.RawBlock('latex', '\\end{minipage}\\par\\vspace{7pt}'))
      open = false
    end
  end
  for _, block in ipairs(doc.blocks) do
    if block.t == 'Header' then
      close_question()
      local label = pandoc.utils.stringify(block.content)
      if block.level == 1 then short_count = 0 end
      if block.level == 1 and label ~= 'How to use this question bank' and label ~= 'Instructions' then
        out:insert(pandoc.RawBlock('latex', '\\clearpage'))
      end
      if block.level == 3 and label:match('%-[MSC]%d%d') then
        open = true
        short = not label:match(' · MC$')
        if is_mock and short then
          if short_count == 4 then out:insert(pandoc.RawBlock('latex', '\\clearpage')) end
          short_count = short_count + 1
        end
        out:insert(pandoc.RawBlock('latex', '\\noindent\\begin{minipage}{\\linewidth}'))
      end
    end
    out:insert(block)
  end
  close_question()
  return pandoc.Pandoc(out, doc.meta)
end
