import System.IO
import Data.Char

nums x = read (filter (\y -> isDigit y || y == '-') x)
lets x = filter isAlpha x

run x v a p | p >= length x = a
            | p `elem` v = 0
            | lets t == "nop" = run x (p:v) a (p+1)
            | lets t == "acc" = run x (p:v) (a+nums t) (p+1)
            | lets t == "jmp" = run x (p:v) a (p+nums t)
 where t = x!!p

makePots x n | n >= length x = []
             | lets t == "jmp" = (fb ++ rep "nop" : sb) : makePots x (n+1)
             | lets t == "nop" = (fb ++ rep "jmp" : sb) : makePots x (n+1)
             | otherwise = x : makePots x (n+1)
 where
  t = x!!n
  fb = fst (splitAt n x)
  rep x = x ++ snd (splitAt 3 t)
  sb = tail (snd (splitAt n x))

main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (maximum (map (\y -> run y [] 0 0) (makePots x 0)))
