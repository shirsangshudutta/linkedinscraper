
profile="""
<div class="entity-result__content entity-result__divider pt3 pb3 t-12 t-black--light">
<div class="mb1">
<div class="linked-area cursor-pointer">
<div class="t-roman t-sans">
<span class="entity-result__title">
<div class="display-flex">
<span class="entity-result__title-line flex-shrink-1 entity-result__title-text--black">
<span class="entity-result__title-text t-16">
<a class="app-aware-link" href="https://www.linkedin.com/in/shanawaz-alam-ju">
<span dir="ltr"><span aria-hidden="true"><!-- -->Shanawaz Alam<!-- --></span><span class="visually-hidden"><!-- -->View Shanawaz Alam’s profile<!-- --></span></span>
</a>
<span class="entity-result__badge t-14 t-normal t-black--light">
<div class="display-flex flex-row-reverse align-items-baseline align-items-center">
<!-- --> <span class="image-text-lockup__text entity-result__badge-text">
<!-- -->• 3rd+<!-- -->
</span>
</div>
</span>
</span>
</span>
<span aria-hidden="true" class="entity-result__badge-overflow align-self-flex-end t-14 t-normal t-black--light flex-shrink-zero">
<div class="display-flex flex-row-reverse align-items-baseline align-items-center">
<!-- --> <span class="image-text-lockup__text entity-result__badge-text">
<!-- -->• 3rd+<!-- -->
</span>
</div>
</span>
</div>
</span>
</div>
<div>
<div class="entity-result__primary-subtitle t-14 t-black">
<!-- -->Final Year Student in Jadavpur University<!-- -->
</div>
<div class="entity-result__secondary-subtitle t-14">
<!-- -->Kolkata<!-- -->
</div>
</div>
</div>
</div>
<div class="linked-area cursor-pointer">
<p class="entity-result__summary t-12 t-black--light">
<!-- -->Education:<span class="white-space-pre"> </span><strong><!-- -->Jadavpur<!-- --></strong><span class="white-space-pre"> </span><!-- --><strong><!-- -->University<!-- --></strong>
</p>
</div>
<!-- --> </div>"""
html1 = BeautifulSoup(profile, 'html.parser')
print(profile)
for b in profile.find_all("span", {"class": "entity-result__title-line flex-shrink-1 entity-result__title-text--black "}):
                print(b)
                # for f in b.find_all("a",{"class":"app-aware-link"}) :
                #     print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&55')