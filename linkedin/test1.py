from bs4 import BeautifulSoup
html="""<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link loading disabled ember-view" data-control-id="kow+GjMESMOT0A99biUo8w==" data-control-name="search_srp_result" href="#" id="ember57"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember58"> <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
<span class="distance-badge hidden separator ember-view" data-test-distance-badge="" id="ember59"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Student at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="klWAiH5iRa+HXLahHJKxdQ==" data-control-name="search_srp_result" href="/in/chandreyee-chowdhury-56244263/" id="ember69"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember70"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Chandreyee Chowdhury</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember71"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Associate Professor at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Past: Research Fellow at Centre for Mobile Computing and Communication (CMCC), <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="tGEYNywnRY25BpeIFGTjeQ==" data-control-name="search_srp_result" href="/in/riya-das-79836817a/" id="ember81"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember82"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Riya Das</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember83"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Student at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="VBqqKT87SWmSbYVqIg1bnw==" data-control-name="search_srp_result" href="/in/ram-sarkar-0ba8a758/" id="ember93"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember94"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Ram Sarkar</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember95"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Associate Professor at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Past: Assistant Professor at <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="LLBMKWSOR0mgUe3IZHY3uA==" data-control-name="search_srp_result" href="/in/ahanadeb/" id="ember105"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember106"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Ahana Deb</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember107"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Student at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>
next_page: &page=2
link1:https://www.linkedin.com/search/results/all/?keywords=jadavpur%20university&origin=GLOBAL_SEARCH_HEADER&&&&&&&&&&&&page=2
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="08iOlQsUSRGOlNr0AlTevg==" data-control-name="search_srp_result" href="/in/professor-somnath-mukherjee-63ab92a0/" id="ember57"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember58"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Professor Somnath Mukherjee</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember59"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Professor at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<!-- -->
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="uXi5A5vsS3C7TQNdMf/ybw==" data-control-name="search_srp_result" href="/in/jadavpur-university-economics-placement-committee-70a489180/" id="ember69"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember70"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Jadavpur University Economics Placement Committee</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember71"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Placement Coordinator at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Summary: <strong>Jadavpur</strong> <strong>University</strong> is one of the best ranked...
      </p>
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="GWleh4mJT46nQSqTnX4bBg==" data-control-name="search_srp_result" href="/in/sonia-mukherjee/" id="ember81"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember82"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Sonia Mukherjee</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember83"><span class="visually-hidden">
    2nd degree connection
</span>
<span class="dist-value">2nd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Systems Engineer, Infosys | Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Bhubaneshwar Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Education: <strong>Jadavpur</strong> <strong>University</strong>
</p>
<div class="search-result__social-proof ember-view" data-test-social-proof-with-names="" id="ember84"> <li-icon aria-hidden="true" class="t-black--light" size="small" type="people-icon"><svg data-supported-dps="16x16" fill="currentColor" focusable="false" height="16" viewbox="0 0 16 16" width="16" xmlns="http://www.w3.org/2000/svg">
<path d="M14.27 9.23l-1.2-.45.31-.51A4.17 4.17 0 0014 6.08V5.5a2.5 2.5 0 00-5 0v.58a4.17 4.17 0 00.62 2.19l.31.51-1.15.43a3.48 3.48 0 00-1-.63L7 8.29v-.56l.25-.41A5 5 0 008 4.69V4a3 3 0 00-6 0v.69a5 5 0 00.75 2.63l.25.41v.56l-.74.29A3.5 3.5 0 000 11.84V13a1 1 0 001 1h14a1 1 0 001-1v-1.25a2.7 2.7 0 00-1.73-2.52zm-3.39-3.85a.63.63 0 011.25 0v1a2.29 2.29 0 01-.34 1.2L11.5 8l-.28-.46a2.29 2.29 0 01-.34-1.2v-1zM4 3.75a1 1 0 012 0v1.44a3 3 0 01-.38 1.46l-.33.6a.25.25 0 01-.22.13h-.14a.25.25 0 01-.22-.13l-.33-.6A3 3 0 014 5.19V3.75zM8 12H2v-.32a1.5 1.5 0 011-1.4l1.5-.58v-.5a2 2 0 00.4.05h.2a2 2 0 00.4-.05v.5l1.5.58a1.5 1.5 0 011 1.4V12zm6.13 0H10v-.16a3.48 3.48 0 00-.24-1.25l1.24-.46v-.38h1v.38l1.54.61a.93.93 0 01.58.87V12z"></path>
</svg></li-icon>
<span class="search-result__social-proof-count t-12 t-black--light ml1">
<span data-entity-hovercard-id="urn:li:fs_miniProfile:ACoAAAK6S24B2eXV112iYNvrabK1RZ05bPES5bU"><a class="li-i18n-linkto search-result__social-proof-link search-result__social-proof-connection-name search-result__social-proof-connection-name--1 t-bold" data-control-id="GWleh4mJT46nQSqTnX4bBg==" data-control-name="view_mutual_connection_profile" href="/in/shirsangshu-dutta-57a3ab13/">Shirsangshu Dutta</a></span> is a shared connection
    </span>
</div>
</div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link loading disabled ember-view" data-control-id="w7KhW3wrQ+6mQfMtybDdbA==" data-control-name="search_srp_result" href="#" id="ember94"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember95"> <span class="name-and-icon"><span class="actor-name">LinkedIn Member</span>
<span class="distance-badge hidden separator ember-view" data-test-distance-badge="" id="ember96"><span class="visually-hidden">
    {:distance}
</span>
<span class="dist-value">{:distance}</span>
</span>
</span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Associate Professor at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<!-- -->
<!-- --> </div>
<div class="search-result__info pt3 pb4 ph0">
<a class="search-result__result-link ember-view" data-control-id="ZSrkAywbTSK//CKvzyrEcg==" data-control-name="search_srp_result" href="/in/sourav-ghosh-779684142/" id="ember106"> <h3 class="actor-name-with-distance search-result__title single-line-truncate ember-view" id="ember107"> <span class="name-and-icon"><span class="name-and-distance">
<span class="name actor-name">Sourav Ghosh</span>
<span class="distance-badge separator ember-view" data-test-distance-badge="" id="ember108"><span class="visually-hidden">
    3rd degree connection
</span>
<span class="dist-value">3rd</span>
</span>
</span><!-- --></span>
</h3>
</a> <p class="subline-level-1 t-14 t-black t-normal search-result__truncate">
        Research Intern at Jadavpur University
    </p>
<p class="subline-level-2 t-12 t-black--light t-normal search-result__truncate">
        Kolkata Area, India
    </p>
<p class="mt2 t-12 t-black--light t-normal search-result__snippets-black">
        Past: Summer Research Intern at <strong>Jadavpur</strong> <strong>University</strong>
</p>
<!-- --> </div>"""
#print(html)
for profile in BeautifulSoup(html,'html.parser').find_all("div",{"class":"search-result__info pt3 pb4 ph0"}):
        if profile is not None:
            #print(profile)
            print('##############')
            # print('profile'+profile.get('href'))
            # link1=profile.find_all("a",{"class":"search-result__result-link ember-view"})
            # link=link1.get('href')
            # print(type(link1))
            for b in profile.find_all("a",{"class":"search-result__result-link ember-view"}):
                 print(b['href'])
            # print('link1'+link1)
            # if link1 is not None:
            #     link='https://www.linkedin.com'+link1['href']
            #     print('link:'+link)