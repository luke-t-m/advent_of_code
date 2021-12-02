import System.IO
import Data.Char




main :: IO ()
main = do
 input <- readFile "input.txt"
 let x = lines input
 print (x)

