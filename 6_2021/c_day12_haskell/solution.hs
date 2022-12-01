import Data.Char
import Data.List
import Data.List.Split


llfind uni x = map last (filter (\t -> head t == x) uni)

nav :: [[String]] -> Bool -> [String] -> String -> [[String]]
nav _ _ _ "end" = [["end"]]
nav uni dob vis cur
 | cur `elem` (delete "start" $ delete "end" vis) && dob==False = concat (map (\t -> map ((:) cur) (nav uni True avis t)) (llfind uni cur))
 | cur `elem` vis = [[cur]]
 | otherwise = concat (map (\t -> map ((:) cur) (nav uni dob avis t)) (llfind uni cur))
  where avis = filter (isLower . head) (cur:vis)

solve uni dob = (filter (\t -> last t == "end") (nav uni dob [] "start"))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = x' ++ (map reverse x') where x' = map (splitOn "-") (lines input)
 print (length (solve x True)) -- part 1
 print (length (solve x False)) -- part 2
 print "done."
