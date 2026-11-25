import pytest
import conversion as con

def test_pulgadas_cm():
assert con.centimetrosApulgadas(5.08) == 2
assert con.pulgadasAcentímeros(2) == 5.08
