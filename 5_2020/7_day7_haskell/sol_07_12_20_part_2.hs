import System.IO
import Data.List.Split

splitAny l x = filter (\y -> y /= "" && y /= "\n") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (splitOn l) x))

sens x = joiner ("0" : splitAny ["bags","bag","contain",","," ","."] x)

joiner (n:a:b:xs) = n : (a ++ " " ++ b) : joiner xs
joiner ("no":["other"]) = ["no other"]
joiner [] = []

locate a x = head (filter (\y -> y!!1 == a) x)

bagger a@(n:b:bs) x | "no other" `elem` a = 1
                    | n == "0" = bagger bs x
                    | otherwise = read n * bagger (locate b x) x + bagger bs x 
bagger [] _ = 1

main :: IO()
main = do
 input <- readFile "input.txt"
 let x = map sens (lines input)
 print ((bagger (locate "shiny gold" x) x)-1)
