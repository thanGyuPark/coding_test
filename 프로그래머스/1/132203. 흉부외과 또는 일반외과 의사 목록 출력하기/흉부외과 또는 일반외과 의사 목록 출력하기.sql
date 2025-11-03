-- DOCTOR 테이블에서 흉부외과(CS) 또는 일반외과(GS) 의사 정보를 조회
SELECT DR_NAME,        -- 의사 이름
       DR_ID,          -- 의사 ID
       MCDP_CD,        -- 진료과 코드
       DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD  -- 고용일자를 YYYY-MM-DD 형식으로 출력
FROM DOCTOR
WHERE MCDP_CD IN ('CS', 'GS')   -- 흉부외과(CS) 또는 일반외과(GS)
ORDER BY HIRE_YMD DESC,          -- 고용일자 오름차순 정렬
         DR_NAME ASC;            -- 같은 날짜면 이름 오름차순 정렬