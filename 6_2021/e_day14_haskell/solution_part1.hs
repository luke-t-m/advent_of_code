import Data.List
import Data.List.Split
import Data.Maybe


step rules i = (head i) : (stepW rules "" i)

stepW rules o i@(a:b:c)
 | lookup (a:[b]) rules /= Nothing = stepW rules (o ++ ((fromJust (lookup (a:[b]) rules)) : [b])) (b:c)
 | otherwise = stepW rules (o ++ [a]) (b:c)
stepW _ o _ = o





conv (x:[y]) = (x, head y)

main :: IO ()
main = do
 input <- readFile "input.txt"
 let template = head (splitOn "\n\n" input)
 let rules = map (conv . splitOn " -> ") (tail (tail (lines input)))

 print ((iterate (step rules) template)!!40)


 print "done."



