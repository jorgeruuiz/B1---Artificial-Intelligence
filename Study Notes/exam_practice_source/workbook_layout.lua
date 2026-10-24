-- Keep each short exam question with its editable, uniquely labelled answer block.
function Pandoc(doc)
  if not FORMAT:match('latex') then return doc end
  doc.meta.lang = nil
  local out = pandoc.List()
  local question_id = nil
  local question_kind = nil
  local function close_question()
    if question_id then
      local height = ({M = '8mm', S = '20mm', C = '26mm'})[question_kind]
      local hint = ({
        M = 'Write A, B, C, or D here. You may add a brief reason.',
        S = 'Write your answer here, usually 1--3 sentences.',
        C = 'Write your short calculation and final result here. Use $...$ or \\[...\\] for maths.'
      })[question_kind]
      out:insert(pandoc.RawBlock('latex',
        '\\begin{solution}[' .. height .. ']{' .. question_id .. '}\n% ' .. hint .. '\n\n\\end{solution}\n\\end{minipage}\\par\\medskip'))
      question_id = nil
    end
  end
  for _, block in ipairs(doc.blocks) do
    if block.t == 'Header' then
      close_question()
      local title = pandoc.utils.stringify(block.content)
      if block.level == 1 then
        out:insert(pandoc.RawBlock('latex', '\\clearpage'))
      elseif block.level == 3 then
        question_id, question_kind = title:match('^([%d%.EL]+%-([MSC])%d%d)')
        if question_id then
          out:insert(pandoc.RawBlock('latex', '% QUESTION ' .. question_id .. '\n\\noindent\\begin{minipage}{\\linewidth}'))
        end
      end
    end
    out:insert(block)
  end
  close_question()
  return pandoc.Pandoc(out, doc.meta)
end
