import Data.List
import Data.List.Split
import Data.Maybe


templater (a:b:c) = ((a:[b]),1) : templater (b:c)
templater _ = []

simplify x = nub (map (\t -> (fst t, (sum (map snd (filter (\s -> (fst s)==(fst t)) x))))) x)

step :: [(String,String)] -> [(String,Int)] -> [(String,Int)]
step rules [] = []
step rules ((a,an):b) = ((head a):m , an) : ((head m):(tail a) , an) : (step rules b)
 where m = fromJust (lookup a rules)

conv (x:[y]) = (x,y)
rev (a,b) = (b,a)

countLetters pCs opCs = simplify (((last (fst (last opCs))), 1) : countLettersW pCs)

countLettersW [] = []
countLettersW ((a,an):b) = simplify ((head a, an) : countLettersW b )

mostTakeLeast x = (fst (last o)) - (fst (head o))
 where o = sort (map rev x)


main :: IO ()
main = do
 input <- readFile "input.txt"
 let opCs = templater (head (splitOn "\n\n" input))
 let rules = map (conv . splitOn " -> ") (tail (tail (lines input)))
 let steps = ((iterate (\t -> simplify (step rules t)) opCs))
 let solve n = mostTakeLeast (countLetters (steps!!n) opCs)
 putStr "Part 1: "
 print (solve 10)
 putStr "Part 2: "
 print (solve 40)
 print "done."



-- turn input into list of (pair, count) tuples
-- step through with set of rules- AB rule C produces pairs AC and BC
-- count letters at end by counting first letter of each pair?
