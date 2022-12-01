import System.IO
import Data.Char
import Data.List.Split

-- redo this, very slow. Different method? Tree?

splitAny l x = filter (\y -> y /= "" && y /= "\n") (splitAnyW l [x])

splitAnyW [] x = x
splitAnyW (l:ls) x = splitAnyW ls (concat (map (splitOn l) x))


sens x = joiner (splitAny ["bags","bag","contain",","," ","."] (filter (not . isDigit) x))

joiner [] = []
joiner (a:b:xs) = (a ++ " " ++ b) : joiner xs


canGold x b | "shiny gold" `elem` b = True
              | "no other" `elem` b = False
              | otherwise = or [canGold x c | c <- x, (head c) `elem` (tail b)]  

trues x = length (filter (==True) x)

main :: IO()
main = do
 input <- readFile "input.txt"
 let x = map sens (lines input)
 print (trues (map (canGold x) x) - 1)
